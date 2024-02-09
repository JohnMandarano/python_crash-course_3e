#Here in my car, I feel safest of all.
def describe_car(make, model, **car_info):
    """Creates and returns a dictionary with information about
    a car """
    car_info['make'] = make
    car_info['model'] = model
    return car_info

#It's really the only way to live.
#In cars.

work_truck = describe_car('toyota', 'tacoma', color='white', is_4wd=False)
print(work_truck)