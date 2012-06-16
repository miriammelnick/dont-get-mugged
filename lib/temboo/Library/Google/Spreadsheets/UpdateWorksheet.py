
###############################################################################
#
# UpdateWorksheet
# Updates existing worksheet metadata such as: Title, Row Count, and Column Count.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateWorksheet(Choreography):

    """
    Create a new instance of the UpdateWorksheet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/UpdateWorksheet')


    def new_input_set(self):
        return UpdateWorksheetInputSet()

    def _make_result_set(self, result, path):
        return UpdateWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateWorksheetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateWorksheet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateWorksheetInputSet(InputSet):
        """
        Set the value of the ColumnCount input for this choreography. ((integer) The number of columns that you want to specify for the worksheet)
        """
        def set_ColumnCount(self, value):
            InputSet._set_input(self, 'ColumnCount', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RowCount input for this choreography. ((integer) The number of rows that you want to specify for the worksheet)
        """
        def set_RowCount(self, value):
            InputSet._set_input(self, 'RowCount', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((string) The unique key associated with the spreadsheet that contains a worksheet you want to update)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Title input for this choreography. ((string) The new title of the worksheet)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google username)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((string) The unique id associated with the worksheet that you want to update)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateWorksheet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateWorksheetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) Response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateWorksheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateWorksheetResultSet(response, path)
