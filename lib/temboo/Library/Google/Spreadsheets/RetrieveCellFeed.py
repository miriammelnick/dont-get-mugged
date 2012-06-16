
###############################################################################
#
# RetrieveCellFeed
# Retrieves a list of cell names and values in a specified Google worksheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveCellFeed(Choreography):

    """
    Create a new instance of the RetrieveCellFeed Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveCellFeed')


    def new_input_set(self):
        return RetrieveCellFeedInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCellFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCellFeedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveCellFeed
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveCellFeedInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((required, string) Your Google password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SpreadsheetKey input for this choreography. ((required, string) The unique for key for the spreadsheet associated with the cells you want to retrieve)
        """
        def set_SpreadsheetKey(self, value):
            InputSet._set_input(self, 'SpreadsheetKey', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google email address)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the WorksheetId input for this choreography. ((required, string) The unique id of the worksheet associated with the cells you want to retrieve)
        """
        def set_WorksheetId(self, value):
            InputSet._set_input(self, 'WorksheetId', value)


"""
A ResultSet with methods tailored to the values returned by the RetrieveCellFeed choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveCellFeedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Google)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveCellFeedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCellFeedResultSet(response, path)
