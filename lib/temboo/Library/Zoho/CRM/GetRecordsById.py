
###############################################################################
#
# GetRecordsById
# Retrieves records from your Zoho CRM account by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetRecordsById(Choreography):

    """
    Create a new instance of the GetRecordsById Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetRecordsById')


    def new_input_set(self):
        return GetRecordsByIdInputSet()

    def _make_result_set(self, result, path):
        return GetRecordsByIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecordsByIdChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetRecordsById
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetRecordsByIdInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID for the Zoho record to lookup)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the GetRecordsById choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetRecordsByIdResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetRecordsByIdChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecordsByIdResultSet(response, path)
