#!/usr/bin/env python
'''
sincos_traits.py - Test program to request sincos recurrence params via Traits.
'''

import sincos

from traits.api import HasTraits, Button, Int, Float
from traitsui.api import Item, Group, View

def doit(x, n):
    '''Calculate sin(i*x),cos(i*x) for i=1..n using recurrence formula.'''
    sc = sincos.sincos_calc_recur(x, n)
    sincos.sincos_print(x, n, sc)
    
# The main demo class:
class SinCosEditorDemo ( HasTraits ):
    """ Defines the TextEditor demo class.
    """

    # Define traits
    button = Button('Calculate')
    theta  = Float(1.0)
    order  = Int(1)

    # TextEditor display with multi-line capability (for a string):
    sincos_group = Group(
        Item( '_' ),
        Item('theta', style='simple', label='Theta'),
        Item('order', style='simple', label='Order'),
        label = 'Sin/Cos Recurrence Params'
    )

    traits_view = View(
        'button',
        sincos_group,
        title   = 'Sin/Cos Recurrence Editor',
        buttons = [ 'OK' ],
        resizable = True,
    )
    
    def _button_fired(self):
        x = self.theta
        n = self.order
        print('BUTTON PRESSED!!!: x = %g, n = %d' % (x, n))
        doit (x, n)
        

# Create the demo:
demo =  SinCosEditorDemo()

# Run the demo (if invoked from the command line):
if __name__ == "__main__":
    demo.configure_traits()
