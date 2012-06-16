
###############################################################################
#
# GetSearchRecordsByPDC
# Retrieves records from your Zoho CRM account and searches by predefined columns.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSearchRecordsByPDC(Choreography):

    """
    Create a new instance of the GetSearchRecordsByPDC Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetSearchRecordsByPDC')


    def new_input_set(self):
        return GetSearchRecordsByPDCInputSet()

    def _make_result_set(self, result, path):
        return GetSearchRecordsByPDCResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSearchRecordsByPDCChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSearchRecordsByPDC
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSearchRecordsByPDCInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the FromIndex input for this choreography. ((optional, integer) The beginning index of the result set to return. Defaults to 1.)
        """
        def set_FromIndex(self, value):
            InputSet._set_input(self, 'FromIndex', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the Module input for this choreography. ((required, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        def set_Module(self, value):
            InputSet._set_input(self, 'Module', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SearchColumn input for this choreography. ((required, string) The column name you want to search (such as "email", the column names used in this method are in lowercase))
        """
        def set_SearchColumn(self, value):
            InputSet._set_input(self, 'SearchColumn', value)

        """
        Set the value of the SearchValue input for this choreography. ((required, string) Specify a search value for the column you're searching)
        """
        def set_SearchValue(self, value):
            InputSet._set_input(self, 'SearchValue', value)

        """
        Set the value of the SelectColumns input for this choreography. ((optional, string) The columns to return separated by commas (i.e. First Name,Last Name,Email). When left empty, only IDs are returned.)
        """
        def set_SelectColumns(self, value):
            InputSet._set_input(self, 'SelectColumns', value)

        """
        Set the value of the ToIndex input for this choreography. ((optional, integer) The ending index of the result set to return. Defaults to 20. Max is 200.)
        """
        def set_ToIndex(self, value):
            InputSet._set_input(self, 'ToIndex', value)


"""
A ResultSet with methods tailored to the values returned by the GetSearchRecordsByPDC choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSearchRecordsByPDCResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSearchRecordsByPDCChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSearchRecordsByPDCResultSet(response, path)
