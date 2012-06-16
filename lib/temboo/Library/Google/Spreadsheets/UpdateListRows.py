
###############################################################################
#
# UpdateListRows
# Updates a worksheet row in a Google spreadsheet using a simple XML file you provide.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateListRows(Choreography):

    """
    Create a new instance of the UpdateListRows Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/UpdateListRows')


    def new_input_set(self):
        return UpdateListRowsInputSet()

    def _make_result_set(self, result, path):
        return UpdateListRowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListRowsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateListRows
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateListRowsInputSet(InputSet):
        """
        Set the value of the RowsetXML input for this choreography. ((XML) The row of data that you want to update in XML format. Your XML needs to be in the rowset/row schema described in the Choreo documentation.)
        """
        def set_RowsetXML(self, value):
            InputSet._set_input(self, 'RowsetXML', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the RowId input for this choreography. ((string) The unique id of the row you want to update)
        """
        def set_RowId(self, value):
            InputSet._set_input(self, 'RowId', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((string) The unique key of the spreadsheet that contains the worksheet you want to update)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Google username)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((string) The unique id of the worksheet that you want to update)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateListRows choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateListRowsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateListRowsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListRowsResultSet(response, path)
