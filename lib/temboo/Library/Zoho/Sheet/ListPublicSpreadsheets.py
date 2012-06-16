
###############################################################################
#
# ListPublicSpreadsheets
# Lists all the spreadsheets that have been made "public" from a user's Zoho Sheet  Account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListPublicSpreadsheets(Choreography):

    """
    Create a new instance of the ListPublicSpreadsheets Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/Sheet/ListPublicSpreadsheets')


    def new_input_set(self):
        return ListPublicSpreadsheetsInputSet()

    def _make_result_set(self, result, path):
        return ListPublicSpreadsheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPublicSpreadsheetsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListPublicSpreadsheets
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListPublicSpreadsheetsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Sets the number of documents to be listed.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the OrderBy input for this choreography. ((optional, string) Order documents by createdTime, lastModifiedTime or name.)
        """
        def set_OrderBy(self, value):
            InputSet._set_input(self, 'OrderBy', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the SortOrder input for this choreography. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        def set_SortOrder(self, value):
            InputSet._set_input(self, 'SortOrder', value)

        """
        Set the value of the StartFrom input for this choreography. ((optional, integer) Sets the initial document number from which the documents will be listed.)
        """
        def set_StartFrom(self, value):
            InputSet._set_input(self, 'StartFrom', value)


"""
A ResultSet with methods tailored to the values returned by the ListPublicSpreadsheets choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListPublicSpreadsheetsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Zoho. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListPublicSpreadsheetsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPublicSpreadsheetsResultSet(response, path)
