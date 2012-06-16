
###############################################################################
#
# DeleteListRow
# Deletes a specified worksheet row from a Google spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteListRow(Choreography):

    """
    Create a new instance of the DeleteListRow Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/DeleteListRow')


    def new_input_set(self):
        return DeleteListRowInputSet()

    def _make_result_set(self, result, path):
        return DeleteListRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteListRowChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteListRow
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteListRowInputSet(InputSet):
        """
        Set the value of the EditLink input for this choreography. ((conditional, string) The entry's edit link URL. Can be retrieved by running RetrieveListFeed and parsing the 'edit' link returned. When the edit link is provided, SpreadhseetKey, WorksheeId, and RowId are not needed.)
        """
        def set_EditLink(self, value):
            InputSet._set_input(self, 'EditLink', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RowId input for this choreography. ((conditional, string) The unique id of the row you want to delete. Required unless providing the EditLink.)
        """
        def set_RowId(self, value):
            InputSet._set_input(self, 'RowId', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((conditional, string) The unique key of the spreadsheet associated with the row you want to delete. Required unless providing the EditLink.)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((conditional, string) The unique id of the worksheet associated with the row you want to delete. Required unless providing the EditLink.)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the DeleteListRow choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteListRowResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteListRowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteListRowResultSet(response, path)
