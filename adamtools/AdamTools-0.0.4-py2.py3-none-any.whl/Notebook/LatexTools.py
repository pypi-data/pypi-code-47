"""
Tools for displaying things in ipython notebooks

Created by adam on 11/11/19
"""
__author__ = 'adam'

from IPython.display import HTML
from IPython.display import display, Latex
from pandas import DataFrame

import io


def convertToLaTeX( df, caption=None, label=None, alignment="c" ):
    """
    Convert a pandas dataframe to a LaTeX tabular.
    Prints labels in bold, does not use math mode
    """
    numColumns = df.shape[ 1 ]
    numRows = df.shape[ 0 ]
    output = io.StringIO()
    colFormat = ("%s|%s" % (alignment, alignment * numColumns))
    # Write header
    output.write( "\\begin{table}[]" )
    output.write( "\\caption{%s} " % caption )
    if label != None:
        output.write( "\\label{%s}" % label )
    output.write( "\\begin{tabular}{%s}\n" % colFormat )
    columnLabels = [ "\\textbf{%s}" % label for label in df.columns ]
    output.write( "& %s\\\\\\hline\n" % " & ".join( columnLabels ) )
    # Write data lines
    for i in range( numRows ):
        output.write( "\\textbf{%s} & %s\\\\\n"
                      % (df.index[ i ], " & ".join( [ str( val ) for val in df.ix[ i ] ] )) )
    # Write footer
    output.write( "\\end{tabular}" )
    output.write( "\\end{table}" )
    return output.getvalue()


def dlatex( df, caption=None, label=None ):
    """
    Does the conversion to latex and does the displaying for ipython
    """
    display( Latex( convertToLaTeX( df, caption, label ) ) )


def fix_percentages_in_axis_description_for_latex( frame ):
    """
    When attempting to display the output of pandas describe() as a latex
    table, the % sign will cause errors. This replaces it with 'th'
    """
    return frame.rename_axis( { '25%': '25th', '50%': '50th', '75%': '75th' } )


def Table( df, caption=None, label=None ):
    """
    Does the conversion to latex and does the displaying for ipython
    """
    display( Latex( convertToLaTeX( df, caption, label ) ) )


def Bold( text ):
    """
    Displays in the ipython way the entered text as latex inside a bold text tag
    """
    display( Latex( '\\textbf{%s}' % text ) )


def StartFigure( caption='', label='' ):
    """
    Displays the LaTex formatting that goes before a figure with caption and label
    @param caption String of caption text
    @param label String of label text
    """
    startstring = "\\begin{figure}[]\caption{%s}\label{%s}" % (caption, label)
    display( Latex( startstring ) )


def StopFigure():
    """
    Displays the LaTex formatting that goes after a figure. Call in separate cell from table maker
    """
    endstring = "\\end{figure}"
    display( Latex( endstring ) )


def Chart( chartFunction, caption='', label='' ):
    startstring = "\\begin{figure}[]\caption{%s}\label{%s}" % (caption, label)
    endstring = "\\end{figure}"
    print( (display( Latex( startstring ) )) )
    chartFunction()
    print( (display( Latex( endstring ) )) )


class Table:
    """
    Used for displaying the data as a formatted html table
    """

    @staticmethod
    def display( data_to_display, title=None ):
        """
        Displays the inputted data as a formatted html table
        @param data_to_display Data in a format that can be made into a pandas DataFrame
        """

        # HTML(
        out = """
        <style type="text/css">
            table.nowrap {
                margin-right: 80px;
            }
            table.dataframe {
                margin-right: 80px;
            }
        </style>"""
        if title != None:
            out += title + DataFrame( data_to_display ).to_html()
        else:
            out += DataFrame( data_to_display ).to_html()

        return HTML( out )

    @staticmethod
    def displaymultiple( list_of_data_to_display, titlelist=None ):
        """
        Displays the inputted data as a formatted html table
        @param data_to_display Data in a format that can be made into a pandas DataFrame
        """
        #
        # HTML("""
        # <style type="text/css">
        #    table.nowrap {
        #        margin-right: 80px;
        #    }
        #    table.dataframe {
        #        margin-right: 80px;
        #    .datatable{
        #        float: left;
        #    }
        #    }
        # </style>""")
        i = 0

        out = """<style type='text/css'>
            table.nowrap {
                margin-right: 80px;
            }
            table.dataframe {
                margin-right: 80px;
            .datatable{
                float: left;
            }
            }
        </style><div class='tables'>"""
        for d in list_of_data_to_display:
            out += "<div class='datatable'>"
            if titlelist != None:
                out += titlelist[ i ]
            out += DataFrame( d ).to_html()
            out += "</div>"
            i += 1
        out += '</div>'

        return HTML( out )


if __name__ == '__main__':
    pass
