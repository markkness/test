#!/usr/bin/env python
'''
sincos_traits.py - Test program to request sincos recurrence params via Traits.
'''

import sincos

# Major library imports
from numpy import exp, linspace, sqrt
from scipy.special import gamma

# Enthought library imports
from enable.api import Component, ComponentEditor
from traits.api import HasTraits, Instance, Button, Int, Float
from traitsui.api import Item, Group, View

# Chaco imports
from chaco.api import ArrayPlotData, Plot
from chaco.tools.api import PanTool, ZoomTool

def doit(x, n):
    '''Calculate sin(i*x),cos(i*x) for i=1..n using recurrence formula.'''
    sc = sincos.sincos_calc_recur(x, n)
    sincos.sincos_print(x, n, sc)

#===============================================================================
# # Create the Chaco plot.
#===============================================================================
def _create_plot_component(all_):

    # Create some x-y data series to plot
    x = linspace(1.0, 8.0, 200)
    pd = ArrayPlotData(index = x)
    pd.set_data("y0", sqrt(x))
    pd.set_data("y1", x)
    pd.set_data("y2", x**2)
    pd.set_data("y3", exp(x))
    pd.set_data("y4", gamma(x))
    pd.set_data("y5", x**x)

    # Create some line plots of some of the data
    plot = Plot(pd)
    plot.plot(("index", "y0"), line_width=2, name="sqrt(x)", color="purple")
    plot.plot(("index", "y1"), line_width=2, name="x", color="blue")
    plot.plot(("index", "y2"), line_width=2, name="x**2", color="green")
    if all_:
        plot.plot(("index", "y3"), line_width=2, name="exp(x)", color="gold")
        plot.plot(("index", "y4"), line_width=2, name="gamma(x)",color="orange")
        plot.plot(("index", "y5"), line_width=2, name="x**x", color="red")

    # Set the value axis to display on a log scale
    plot.value_scale = "log"

    # Tweak some of the plot properties
    plot.title = "Log Plot"
    plot.padding = 50
    plot.legend.visible = True

    # Attach some tools to the plot
    plot.tools.append(PanTool(plot))
    zoom = ZoomTool(component=plot, tool_mode="box", always_on=False)
    plot.overlays.append(zoom)

    return plot

def _create_plot_component2(pd, all_):

    ## Create some x-y data series to plot
    #x = linspace(1.0, 8.0, 200)
    #pd = ArrayPlotData(index = x)
    #pd.set_data("y0", sqrt(x))
    #pd.set_data("y1", x)
    #pd.set_data("y2", x**2)
    #pd.set_data("y3", exp(x))
    #pd.set_data("y4", gamma(x))
    #pd.set_data("y5", x**x)

    # Create some line plots of some of the data
    plot = Plot(pd)
    plot.plot(("index", "y0"), line_width=2, name="sqrt(x)", color="purple")
    plot.plot(("index", "y1"), line_width=2, name="x", color="blue")
    plot.plot(("index", "y2"), line_width=2, name="x**2", color="green")
    if all_:
        plot.plot(("index", "y3"), line_width=2, name="exp(x)", color="gold")
        plot.plot(("index", "y4"), line_width=2, name="gamma(x)",color="orange")
        plot.plot(("index", "y5"), line_width=2, name="x**x", color="red")

    # Set the value axis to display on a log scale
    plot.value_scale = "log"

    # Tweak some of the plot properties
    plot.title = "Log Plot"
    plot.padding = 50
    plot.legend.visible = True

    # Attach some tools to the plot
    plot.tools.append(PanTool(plot))
    zoom = ZoomTool(component=plot, tool_mode="box", always_on=False)
    plot.overlays.append(zoom)

    return plot

def plot_stuff(plot, all_):
    '''Plot some curves.'''
    # Create some x-y data series to plot
    x = linspace(1.0, 8.0, 200)
    pd = ArrayPlotData(index = x)
    pd.set_data("y0", sqrt(x))
    pd.set_data("y1", x)
    pd.set_data("y2", x**2)
    if all_:
        pd.set_data("y3", exp(x))
        pd.set_data("y4", gamma(x))
        pd.set_data("y5", x**x)

    # Create some line plots of some of the data
    #plot = Plot(pd)
    plot.plot(("index", "y0"), line_width=2, name="sqrt(x)", color="purple")
    plot.plot(("index", "y1"), line_width=2, name="x", color="blue")
    plot.plot(("index", "y2"), line_width=2, name="x**2", color="green")
    if all_:
        plot.plot(("index", "y3"), line_width=2, name="exp(x)", color="gold")
        plot.plot(("index", "y4"), line_width=2, name="gamma(x)",color="orange")
        plot.plot(("index", "y5"), line_width=2, name="x**x", color="red")

    # Set the value axis to display on a log scale
    plot.value_scale = "log"

    # Tweak some of the plot properties
    plot.title = "Log Plot"
    plot.padding = 50
    plot.legend.visible = True

    ## Attach some tools to the plot
    #plot.tools.append(PanTool(plot))
    #zoom = ZoomTool(component=plot, tool_mode="box", always_on=False)
    #plot.overlays.append(zoom)

    #return plot
    
# The main demo class:
class SinCosEditorDemo(HasTraits):
    """ Defines the TextEditor demo class.
    """

    plot = Instance(Component)
    # Define traits
    button = Button('Calculate')
    button2 = Button('Bozo')
    theta  = Float(1.0)
    order  = Int(1)

    #def setup_data(self, th, n):
    #    # Create some x-y data series to plot
    #    self.x = linspace(1.0, 8.0, 200)
    #    self.pd = ArrayPlotData(index = self.x)
    #    self.pd.set_data("y0", sqrt(self.x))
    #    self.pd.set_data("y1", self.x)
    #    self.pd.set_data("y2", self.x ** 2)
    #    self.pd.set_data("y3", exp(self.x))
    #    self.pd.set_data("y4", gamma(self.x))
    #    self.pd.set_data("y5", self.x ** self.x)

    #setup_data(theta, order)
    # Create some x-y data series to plot
    x = linspace(1.0, 8.0, 200)
    pd = ArrayPlotData(index = x)
    pd.set_data("y0", sqrt(x))
    pd.set_data("y1", x)
    pd.set_data("y2", x**2)
    pd.set_data("y3", exp(x))
    pd.set_data("y4", gamma(x))
    pd.set_data("y5", x**x)

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

    traits_view = View(
        'button',
        'button2',
        sincos_group,
        plot_group,
        title   = 'Sin/Cos Recurrence Editor',
        buttons = [ 'OK' ],
        resizable = True,
    )
    
    def _button_fired(self):
        th = self.theta
        n  = self.order
        print('BUTTON PRESSED!!!: th = %g, n = %d' % (th, n))
        doit (th, n)
        #plot = _create_plot_component(True)
        #plot_stuff(self.plot, True)
        self.pd.set_data("y0", exp(self.x))
        self.pd.set_data("y1", gamma(self.x))
        self.pd.set_data("y2", self.x**self.x)

    def _button2_fired(self):
        print('BOZO')
        #self.setup_data(self.theta, self.order)
                        
    def _plot_default(self):
         #return _create_plot_component(False)
         return _create_plot_component2(self.pd,False)

# Create the demo:
demo = SinCosEditorDemo()
#demo.setup_data (1.0, 1)

# Run (if invoked from the command line):
if __name__ == "__main__":
    demo.configure_traits()
