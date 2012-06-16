
###############################################################################
#
# GetWebsiteLocalesForSyndicationService
# Returns the list of supported website locales (languages) for a given type of SyndicationService.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetWebsiteLocalesForSyndicationService(Choreography):

    """
    Create a new instance of the GetWebsiteLocalesForSyndicationService Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/AdSenseHost/AccountService/GetWebsiteLocalesForSyndicationService')


    def new_input_set(self):
        return GetWebsiteLocalesForSyndicationServiceInputSet()

    def _make_result_set(self, result, path):
        return GetWebsiteLocalesForSyndicationServiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWebsiteLocalesForSyndicationServiceChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetWebsiteLocalesForSyndicationService
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetWebsiteLocalesForSyndicationServiceInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the GetWebsiteLocalesForSyndicationService choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetWebsiteLocalesForSyndicationServiceResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Google AdSense.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetWebsiteLocalesForSyndicationServiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWebsiteLocalesForSyndicationServiceResultSet(response, path)
