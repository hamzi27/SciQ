from flask import Flask
from flask import Markup
value = Markup('<strong>The HTML String</strong>')


class Exp:
    pass


def return_object():
  response_obj = Exp()
  response_obj.success = True
  response_obj.query = 'x^3 - y^2 = 23'
  response_obj.execution_time = '1.744' 
  response_obj.plots = ['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']
  response_obj.alternate_forms = [Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mrow>  <msup>   <mi>x</mi>   <mn>3</mn>  </msup>  <mo>=</mo>  <mrow>   <msup>    <mi>y</mi>    <mn>2</mn>   </msup>   <mo>+</mo>   <mn>23</mn>  </mrow> </mrow></math>"), Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mrow>  <mrow>   <msup>    <mi>x</mi>    <mn>3</mn>   </msup>   <mo>-</mo>   <msup>    <mi>y</mi>    <mn>2</mn>   </msup>   <mo>-</mo>   <mn>23</mn>  </mrow>  <mo>=</mo>  <mn>0</mn> </mrow></math>")]
  response_obj.results = []
  response_obj.solutions = [Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mtable displaystyle='true'>  <mtr>   <mtd>    <mrow>     <mrow>      <mi>x</mi>      <mo>=</mo>      <mn>3</mn>     </mrow>     <mtext>,   </mtext>     <mrow>      <mi>y</mi>      <mo>=</mo>      <mrow>       <mo>&#177;</mo>       <mn>2</mn>      </mrow>     </mrow>    </mrow>   </mtd>  </mtr> </mtable></math>")]
  response_obj.symbolic_solutions = [Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mtable displaystyle='true'>  <mtr>   <mtd>    <mrow>     <mi>y</mi>     <mo>=</mo>     <mrow>      <mo>-</mo>      <msqrt>       <mrow>        <msup>         <mi>x</mi>         <mn>3</mn>        </msup>        <mo>-</mo>        <mn>23</mn>       </mrow>      </msqrt>     </mrow>    </mrow>   </mtd>  </mtr> </mtable></math>"), Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mtable displaystyle='true'>  <mtr>   <mtd>    <mrow>     <mi>y</mi>     <mo>=</mo>     <msqrt>      <mrow>       <msup>        <mi>x</mi>        <mn>3</mn>       </msup>       <mo>-</mo>       <mn>23</mn>      </mrow>     </msqrt>    </mrow>   </mtd>  </mtr> </mtable></math>")] 
  response_obj.limits = []
  response_obj.partial_derivatives = [Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mrow>  <mfrac>   <mrow>    <mi>d</mi>    <mo>&#8290;</mo>    <mrow>     <mi>x</mi>     <mo>&#8289;</mo>     <mo>(</mo>     <mi>y</mi>     <mo>)</mo>    </mrow>   </mrow>   <mrow>    <mi>d</mi>    <mo>&#8290;</mo>    <mi>y</mi>   </mrow>  </mfrac>  <mo>=</mo>  <mfrac>   <mrow>    <mn>2</mn>    <mo>&#8290;</mo>    <mi>y</mi>   </mrow>   <mrow>    <mn>3</mn>    <mo>&#8290;</mo>    <msup>     <mi>x</mi>     <mn>2</mn>    </msup>   </mrow>  </mfrac> </mrow></math>"), Markup("<math xmlns='http://www.w3.org/1998/Math/MathML'    mathematica:form='StandardForm'    xmlns:mathematica='http://www.wolfram.com/XML/'> <mrow>  <mfrac>   <mrow>    <mi>d</mi>    <mo>&#8290;</mo>    <mrow>     <mi>y</mi>     <mo>&#8289;</mo>     <mo>(</mo>     <mi>x</mi>     <mo>)</mo>    </mrow>   </mrow>   <mrow>    <mi>d</mi>    <mo>&#8290;</mo>    <mi>x</mi>   </mrow>  </mfrac>  <mo>=</mo>  <mfrac>   <mrow>    <mn>3</mn>    <mo>&#8290;</mo>    <msup>     <mi>x</mi>     <mn>2</mn>    </msup>   </mrow>   <mrow>    <mn>2</mn>    <mo>&#8290;</mo>    <mi>y</mi>   </mrow>  </mfrac> </mrow></math>")]
  response_obj.integral = []
  return response_obj




  # response_obj.query (in latex)
    # response_obj.success (boolean)
    # responde_obj.execution_time
    # responde_obj.plots = (array di path se passiamo id_equation, altrimenti base_64)
    # response_obj.alternate_forms = (array di mathml)
    # response_obj.results = (array di mathml)
    # response_obj.solutions = (array di mathml)
    # response_obj.symbolic_solutions = (array di mathml)
    # response_obj.limits = (array di mathml)
    # response_obj.partial_derivatives = (array di mathml)
    # response_obj.integral = (array di mathml)
