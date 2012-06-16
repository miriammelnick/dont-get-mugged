
###############################################################################
#
# GetSyndicationService
# Returns the service data for the SyndicationService (returns either 'ContentAds' or 'SearchAds').
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetSyndicationService(Choreography):

    """
    Create a new instance of the GetSyndicationService Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/GetSyndicationService')


    def new_input_set(self):
        return GetSyndicationServiceInputSet()

    def _make_result_set(self, result, path):
        return GetSyndicationServiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSyndicationServiceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetSyndicationService
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetSyndicationServiceInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((string) The ID of the publisher to get the syndication service data from.)
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
        Set the value of the SynServiceType input for this choreography. ((string) One of 'ContentAds' or 'SearchAds'.)
        """
        def set_SynServiceType(self, value):
            InputSet._set_input(self, 'SynServiceType', value)


"""
A ResultSet with methods tailored to the values returned by the GetSyndicationService choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetSyndicationServiceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetSyndicationServiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSyndicationServiceResultSet(response, path)
