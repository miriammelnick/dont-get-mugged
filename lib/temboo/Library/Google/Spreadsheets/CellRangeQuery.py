
###############################################################################
#
# CellRangeQuery
# Retrieves a range of cells from a specified Google worksheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CellRangeQuery(Choreography):

    """
    Create a new instance of the CellRangeQuery Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/CellRangeQuery')


    def new_input_set(self):
        return CellRangeQueryInputSet()

    def _make_result_set(self, result, path):
        return CellRangeQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CellRangeQueryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CellRangeQuery
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CellRangeQueryInputSet(InputSet):
        """
        Set the value of the MaxColumn input for this choreography. ((optional, integer) The maximum column number for the cell range that you want to retrieve)
        """
        def set_MaxColumn(self, value):
            InputSet._set_input(self, 'MaxColumn', value)

        """
        Set the value of the MaxRow input for this choreography. ((optional, integer) The maximum row number for the cell range that you want to retrieve)
        """
        def set_MaxRow(self, value):
            InputSet._set_input(self, 'MaxRow', value)

        """
        Set the value of the MinColumn input for this choreography. ((optional, integer) The minimum column number for the cell range you want to retrieve)
        """
        def set_MinColumn(self, value):
            InputSet._set_input(self, 'MinColumn', value)

        """
        Set the value of the MinRow input for this choreography. ((optional, integer) The minimum row number for the cell range you want to retrieve)
        """
        def set_MinRow(self, value):
            InputSet._set_input(self, 'MinRow', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((string) The unique for key for the spreadsheet associated with the cells you want to retrieve)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((string) The unique id of the worksheet associated with the cells you want to retrieve)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the CellRangeQuery choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CellRangeQueryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CellRangeQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CellRangeQueryResultSet(response, path)
