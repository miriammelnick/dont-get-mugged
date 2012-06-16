
###############################################################################
#
# GetCVRecord
# Retrieves records from your Zoho CRM account by customer view.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCVRecord(Choreography):

    """
    Create a new instance of the GetCVRecord Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetCVRecord')


    def new_input_set(self):
        return GetCVRecordInputSet()

    def _make_result_set(self, result, path):
        return GetCVRecordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCVRecordChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCVRecord
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCVRecordInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CVName input for this choreography. ((optional, string) Used to retrieve records from a specific customer view. Defaults to 'All Open Leads'.)
        """
        def set_CVName(self, value):
            InputSet._set_input(self, 'CVName', value)

        """
        Set the value of the FromIndex input for this choreography. ((optional, integer) The beginning index of the result set to return. Defaults to 1.)
        """
        def set_FromIndex(self, value):
            InputSet._set_input(self, 'FromIndex', value)

        """
        Set the value of the LastModifiedDate input for this choreography. ((optional, date) Used to return records with a created or modified date that is after the specified time.  (i.e. 2010-04-21 11:09:23))
        """
        def set_LastModifiedDate(self, value):
            InputSet._set_input(self, 'LastModifiedDate', value)

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
        Set the value of the ToIndex input for this choreography. ((optional, integer) The ending index of the result set to return. Defaults to 20. Max is 200.)
        """
        def set_ToIndex(self, value):
            InputSet._set_input(self, 'ToIndex', value)


"""
A ResultSet with methods tailored to the values returned by the GetCVRecord choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCVRecordResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCVRecordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCVRecordResultSet(response, path)
