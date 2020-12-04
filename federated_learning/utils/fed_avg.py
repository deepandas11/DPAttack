import torch
from numpy import linalg as la
import math
import numpy


def calculate_parameter_gradients(params_1, params_2):

    return numpy.array([x for x in numpy.subtract(params_1, params_2)])

def is_benign(grad_norm, bookkeeper):
    return bookkeeper.thresh1 <= grad_norm <= bookkeeper.thresh2

def average_nn_parameters(parameters, curr_parameters, epoch, bookkeeper):
    """
    Averages passed parameters.

    :param parameters: nn model named parameters
    :type parameters: list
    """
    # Compute norm here if within  a range
    # curr_grad_norms = compute_gradients(curr_parameters, parameters)
    curr_grad_vecs = compute_grad_vecs(curr_parameters, parameters)
    if 10 <= epoch <= 50:
        # bookkeeper.add_to_book(curr_grad_norms)
        bookkeeper.add_to_book(curr_grad_vecs)
        if epoch == 50:
            # bookkeeper.compute_thresholds()
            bookkeeper.compute_avg_vec()

    # if epoch >= 51:
    #     new_parameters = []
    #     for i, grad_norm in enumerate(curr_grad_norms):
    #         if is_benign(grad_norm, bookkeeper):
    #             new_parameters.append(parameters[i])
    #     if len(new_parameters) == 0:
    #         return curr_parameters, bookkeeper
    #     else:
    #         parameters = new_parameters



    if epoch >= 50:
        current_gradient_vecs = []
        for grad_vec in curr_grad_vecs:
            if la.norm(grad_vec) != 0:
                current_gradient_vecs.append(grad_vec/la.norm(grad_vec))
            else:
                current_gradient_vecs.append(grad_vec)

        current_gradient_sims = numpy.array(
            [numpy.dot(bookkeeper.mean_vec, grad_vec) for grad_vec in current_gradient_vecs]
        )
        client_logits = [numpy.exp(item) for item in current_gradient_sims]
        denom = sum(client_logits)
        client_weights = [item/denom for item in client_logits]
        new_params = {}
        for name in parameters[0].keys():
            new_params[name] = sum(
                [client_weights[i]*param[name].data for i, param in enumerate(parameters)]
            )
            # print(new_params[name])
        return new_params, bookkeeper

    new_params = {}
    for name in parameters[0].keys():
        new_params[name] = torch.true_divide(sum([param[name].data for param in parameters]), len(parameters))

    return new_params, bookkeeper



def get_layer_params(params, layer_num):
    ans =  params[layer_num].detach().cpu().numpy()
    return ans


def compute_gradients(old_params, new_params, layer_name='fc2.weight'):

    worker_dict = []
    for i, new_param in enumerate(new_params):
        l2s = []
        for class_num in range(10):
            start_model_layer_param = list(get_layer_params(old_params, layer_name)[class_num])
            end_model_layer_param = list(get_layer_params(new_param, layer_name)[class_num])
            grad = calculate_parameter_gradients(start_model_layer_param, end_model_layer_param)
            grad = grad.flatten()
            l2s.append(la.norm(grad))

        worker_dict.append(la.norm(numpy.array(l2s)))

    return worker_dict

def compute_grad_vecs(old_params, new_params, layer_name='fc2.weight'):

    worker_list = []
    for i, new_param in enumerate(new_params):
        l2s = []
        for class_num in range(10):
            start_model_layer_param = list(get_layer_params(old_params, layer_name)[class_num])
            end_model_layer_param = list(get_layer_params(new_param, layer_name)[class_num])
            grad = calculate_parameter_gradients(start_model_layer_param, end_model_layer_param)
            grad = grad.flatten()
            l2s.append(la.norm(grad))

        l2s = numpy.array(l2s)
        worker_list.append(l2s)

    return worker_list
