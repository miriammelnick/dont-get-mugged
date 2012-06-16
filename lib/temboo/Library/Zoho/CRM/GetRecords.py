
###############################################################################
#
# GetRecords
# Retrieves records from your Zoho CRM account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecords(Choreography):

    """
    Create a new instance of the GetRecords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetRecords')


    def new_input_set(self):
        return GetRecordsInputSet()

    def _make_result_set(self, result, path):
        return GetRecordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecordsInputSet(InputSet):
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
        Set the value of the LastModifiedTime input for this choreography. ((optional, date) Used to return records with a created or modified date that is after the specified time.  (i.e. 2010-04-21 11:09:23))
        """
        def set_LastModifiedTime(self, value):
            InputSet._set_input(self, 'LastModifiedTime', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the Module input for this choreography. ((optional, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        def set_Module(self, value):
            InputSet._set_input(self, 'Module', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SelectColumns input for this choreography. ((optional, string) The columns to return separated by commas (i.e. First Name,Last Name,Email). When left empty, only IDs are returned.)
        """
        def set_SelectColumns(self, value):
            InputSet._set_input(self, 'SelectColumns', value)

        """
        Set the value of the SortColumnString input for this choreography. ((required, string) Used to specify a column to sort by (in ascending order))
        """
        def set_SortColumnString(self, value):
            InputSet._set_input(self, 'SortColumnString', value)

        """
        Set the value of the SortOrderString input for this choreography. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        def set_SortOrderString(self, value):
            InputSet._set_input(self, 'SortOrderString', value)

        """
        Set the value of the ToIndex input for this choreography. ((optional, integer) The ending index of the result set to return. Defaults to 20. Max is 200.)
        """
        def set_ToIndex(self, value):
            InputSet._set_input(self, 'ToIndex', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecordsResultSet(response, path)
