widgets = int(input("No. of widgets: "))
gizmos = int(input("No. of gizmos: "))

w_widgets = widgets * 75
w_gizmos = gizmos * 112
w_total = w_widgets + w_gizmos

print('Gizmos weigh {:d}g and Widgets weigh {:d}g. Total weight is {:d}g.'.format(w_gizmos, w_widgets, w_total))
