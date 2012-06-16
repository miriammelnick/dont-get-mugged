
###############################################################################
#
# DeleteWorksheet
# Deletes a specified worksheet from an existing spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteWorksheet(Choreography):

    """
    Create a new instance of the DeleteWorksheet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/DeleteWorksheet')


    def new_input_set(self):
        return DeleteWorksheetInputSet()

    def _make_result_set(self, result, path):
        return DeleteWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteWorksheetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteWorksheet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteWorksheetInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((string) The unique key associated with the spreadsheet that contains a worksheet you want to delete)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google username)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((string) The unique id associated with the worksheet that you want to delete)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteWorksheet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteWorksheetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteWorksheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteWorksheetResultSet(response, path)
