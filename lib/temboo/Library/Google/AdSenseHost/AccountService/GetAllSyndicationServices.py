
###############################################################################
#
# GetAllSyndicationServices
# Returns data about all the SyndicationService services ('ContentAds' or 'SearchAds') subscribed to by the publisher.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetAllSyndicationServices(Choreography):

    """
    Create a new instance of the GetAllSyndicationServices Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/GetAllSyndicationServices')


    def new_input_set(self):
        return GetAllSyndicationServicesInputSet()

    def _make_result_set(self, result, path):
        return GetAllSyndicationServicesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllSyndicationServicesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetAllSyndicationServices
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetAllSyndicationServicesInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((string) The ID of the publisher to get the syndications services of.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Email input for this choreography. ((string) The developer's email address.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Endpoint input for this choreography. ((optional, string) One of either 'sandbox.google.com' (for testing) or 'www.google.com'. Defaults to 'sandbox.google.com'.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the Password input for this choreography. ((string) The developer's password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the GetAllSyndicationServices choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetAllSyndicationServicesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetAllSyndicationServicesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllSyndicationServicesResultSet(response, path)
