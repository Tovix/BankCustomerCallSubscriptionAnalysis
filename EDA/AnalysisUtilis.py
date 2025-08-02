import os
import contextlib
import streamlit as st
from io import StringIO
from functools import wraps
import matplotlib.pyplot as plt

class AnalysisHelperFunctions:
      figuresFilePath = "Figures/"
      
      @staticmethod
      def savePlotFigure(filename: str) -> None:
            savePath = AnalysisHelperFunctions.figuresFilePath + filename
            os.makedirs(os.path.dirname(savePath), exist_ok=True)
            if not os.path.exists(savePath):
                  plt.savefig(savePath)
                  print(f"Plot saved to {savePath}")
            else:
                  print(f"File {savePath} already exists. Plot not saved.")
      
      @staticmethod
      def streamLitPlotDisplay(func):
            """Decorator to automatically display matplotlib plots in Streamlit.
            
            Handles figure cleanup and supports both plt.show() and figure object return patterns.
            """
            @wraps(func)
            def wrapper(*args, **kwargs):
                  result = func(*args, **kwargs)
                  display_fig = result if isinstance(result, plt.Figure) else plt.gcf()
                  st.pyplot(display_fig, use_container_width=False)
                  plt.close('all')
                  return result
            return wrapper
      
      @staticmethod
      def streamlitPrintOutput(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                  with st.empty():
                        output = StringIO()
                        with contextlib.redirect_stdout(output):
                              result = func(*args, **kwargs)
                        if output.getvalue():
                              st.text(output.getvalue())
                  if result is not None:
                        st.write("Return value:", result)
                  return result
            return wrapper