
###############################################################################
#
# GetCompanyProfiles
# Retrieve multiple company profiles using a given list of company IDs or names.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetCompanyProfiles(Choreography):

    """
    Create a new instance of the GetCompanyProfiles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Companies/GetCompanyProfiles')


    def new_input_set(self):
        return GetCompanyProfilesInputSet()

    def _make_result_set(self, result, path):
        return GetCompanyProfilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompanyProfilesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetCompanyProfiles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCompanyProfilesInputSet(InputSet):
        """
        Set the value of the Companies input for this choreography. ((required, string) A comma separated list of company IDs or universal-name key/value pairs. IDs and names can be mixed also. For example: 812686,universal-name=linkedin,universal-name=apple.)
        """
        def set_Companies(self, value):
            InputSet._set_input(self, 'Companies', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by LinkedIn after registering your application.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)


"""
A ResultSet with methods tailored to the values returned by the GetCompanyProfiles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCompanyProfilesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from LinkedIn in XML format.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCompanyProfilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompanyProfilesResultSet(response, path)
