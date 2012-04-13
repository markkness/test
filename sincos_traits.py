#!/usr/bin/env python
'''
sincos_traits.py - Test program to request sincos recurrence params via Traits.
'''

import sincos

import pdb
import math

# Major library imports
import numpy
from numpy import linspace, sin, cos

# Enthought library imports
from enable.api import Component, ComponentEditor
from traits.api import HasTraits, Instance, Button, Array, Int, Float
from traitsui.api import Item, Group, View
from traitsui.ui_editors.array_view_editor import ArrayViewEditor

# Chaco imports
from chaco.api import ArrayPlotData, Plot
from chaco.tools.api import PanTool, ZoomTool

def doit(x, n):
    '''Calculate sin(i*x),cos(i*x) for i=1..n using recurrence formula.'''
    sc = sincos.sincos_calc_recur(x, n)
    sincos.sincos_print(x, n, sc)
    return sc

#===============================================================================
# # Create the Chaco plot.
#===============================================================================

def _create_plot_component(pd):
    plot = Plot(pd)
    
    # analytic curves for sin(x),cos(x)
    plot.plot(("x0", "y0"), line_width=2, name="sin(x)", color="purple")
    plot.plot(("x0", "y1"), line_width=2, name="cos(x)", color="blue")
    # discrete recurrence values Sn,Cn
    plot.plot(("x1", "y2"), type="scatter", name="Sn", color="green")
    plot.plot(("x1", "y3"), type="scatter", name="Cn", color="gold")

    # Tweak some of the plot properties
    plot.title = "Sin/Cos"
    plot.padding = 50
    plot.legend.visible = True

    # Attach some tools to the plot
    plot.tools.append(PanTool(plot))
    zoom = ZoomTool(component=plot, tool_mode="box", always_on=False)
    plot.overlays.append(zoom)

    return plot

# The main demo class:
class SinCosEditorDemo(HasTraits):
    '''Plotting example that calculates sin/cos analytically and via recurrence.'''

    plot = Instance(Component)
    button = Button('Calculate')
    theta  = Float(0.1)
    order  = Int(10)
    data = Array
    pd = ArrayPlotData()

    def __init__(self):
        super(SinCosEditorDemo, self).__init__()

    def setup_data(self):
        # Get table of recurrence values
        th = self.theta
        n  = self.order
        self.data = doit (th, n)
        # x values for recurrence
        self.xn = numpy.empty ((n))
        for i in range(n):
            self.xn[i] = (i + 1) * th
        # y values for recurrence
        y2 = self.data[:,0]
        y3 = self.data[:,1]
        # plotdata for recurrence values
        self.pd.set_data("x1", self.xn)
        self.pd.set_data("y2", y2)
        self.pd.set_data("y3", y3)
        # x values for analytic curves
        xmin = 0.001
        xmax = 2.0 * (n + 1) * th
        # at least 100 points per period
        npts0 = round (100 * n * th / (2.0*math.pi))
        # at least 200 points total
        npts1 = 200
        npts = max(npts0, npts1)
        #print('npts = %d [npts0 = %d, npts1 = %d]' % (npts, npts0, npts1))
        self.x = linspace(xmin, xmax, npts)
        # y values for analytic curves
        y0 = sin(self.x)
        y1 = cos(self.x)
        # plotdata for analytic curves
        self.pd.set_data("x0", self.x)
        self.pd.set_data("y0", y0)
        self.pd.set_data("y1", y1)

    # TextEditor display with multi-line capability (for a string):
    sincos_group = Group(
        Item( '_' ),
        Item('theta', style='simple', label='Theta'),
        Item('order', style='simple', label='Order'),
        label = 'Sin/Cos Recurrence Params',
    )

    plot_group = Group(
        Item(
            'plot', 
            editor=ComponentEditor(size=(800,400)),
            show_label=False),
        orientation = "vertical",
    )

    table_titles = ['sin((n+1)*x)', 'cos((n+1)*x)']
    table_group = Group(
        Item(
            'data',
            editor=ArrayViewEditor(titles=table_titles, format='%.6f'),
            show_label=False),
    )

    traits_view = View(
        'button',
        sincos_group,
        plot_group,
        table_group,
        title   = 'Sin/Cos Recurrence Editor',
        buttons = [ 'OK' ],
        resizable = True,
    )
    
    def _button_fired(self):
        print('BUTTON PRESSED!!!')
        self.setup_data()

    def _plot_default(self):
         return _create_plot_component(self.pd)

# Create the demo:
demo = SinCosEditorDemo()
demo.setup_data()

# Run (if invoked from the command line):
if __name__ == "__main__":
    demo.configure_traits()
