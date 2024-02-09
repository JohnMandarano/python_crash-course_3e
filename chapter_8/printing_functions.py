def print_models(unprinted_models, completed_models):
    """Simulate printing each model until none are left.
    Move each design to completed models when done
    """
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}.")
        completed_models.append(current_model)

def show_completed_models(completed_models):
    """Show all models that were completed."""
    print("\nThe following models have been completed.")
    for completed_model in completed_models:
        print(completed_model)