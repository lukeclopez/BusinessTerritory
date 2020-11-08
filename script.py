from shapely.geometry import Point, Polygon

# Create Point objects
points_to_check = {
    'ymca': Point(27.892777, -82.248241),
    'hopewell': Point(27.921328, -82.140049),
}

# Create a Polygon
coords = [
    (27.863526,-82.249352),
    (27.885334, -82.224783),
    (27.893623, -82.232916),
    (27.897030, -82.242618),
    (27.894764, -82.255494)
]
territory = Polygon(coords)

for name, point in points_to_check.items():
    res = territory.contains(point)
    print(f'{name} in territory: {res}')