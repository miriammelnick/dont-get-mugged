
###############################################################################
#
# UpdateCells
# Updates a specified cell in a Google worksheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateCells(Choreography):

    """
    Create a new instance of the UpdateCells Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/UpdateCells')


    def new_input_set(self):
        return UpdateCellsInputSet()

    def _make_result_set(self, result, path):
        return UpdateCellsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCellsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateCells
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateCellsInputSet(InputSet):
        """
        Set the value of the Column input for this choreography. ((required, integer) The column number of the cell location that you want to update (for example, column A = 1, columnB = 2, etc).)
        """
        def set_Column(self, value):
            InputSet._set_input(self, 'Column', value)

        """
        Set the value of the InputValue input for this choreography. ((required, string) The new value for the cell)
        """
        def set_InputValue(self, value):
            InputSet._set_input(self, 'InputValue', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Row input for this choreography. ((required, integer) The row number of the cell location that you want to update)
        """
        def set_Row(self, value):
            InputSet._set_input(self, 'Row', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((required, string) The unique for key for the spreadsheet associated with the cell you want to update)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((required, string) The unique id of the worksheet associated with the cell you want to update)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateCells choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateCellsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateCellsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateCellsResultSet(response, path)
