import matplotlib.pyplot as plt
import numpy as np

def plot_figures_for_cv(l_iwls_vals_list, l_sgd_vals_list, l_adam_vals_list):
    """Function plots Minus log likelihood vs Iteration number for each model and fold from CV"""
    n_folds = len(l_iwls_vals_list)
    for i in range(n_folds):
        
        l_iwls_vals = l_iwls_vals_list[i]
        l_sgd_vals = l_sgd_vals_list[i]
        l_adam_vals = l_adam_vals_list[i]
        
        plt.figure(figsize=(15, 8))
        plt.plot(np.linspace(1, len(l_iwls_vals), len(l_iwls_vals)), l_iwls_vals, label="IWLS")
        plt.plot(np.linspace(1, len(l_sgd_vals), len(l_sgd_vals)), l_sgd_vals, label="SGD")
        plt.plot(np.linspace(1, len(l_adam_vals), len(l_adam_vals)), l_adam_vals, label="ADAM")
        plt.legend()
        plt.rc('xtick', labelsize=10)
        plt.rc('ytick', labelsize=10)
        plt.rc('legend', fontsize=15)
        plt.xlabel("Iterations", fontsize=20)
        plt.ylabel("Minus log-likelihood", fontsize=20)
        plt.title(f"Comparison between models for fold {i+1}", fontsize=20)
        plt.show()   