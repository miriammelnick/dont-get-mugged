
###############################################################################
#
# VenueDetail
# Obtain details about venues, including location, mayorship, tags, tips, specials and category.  Users who have authenticated via their oauth_token credential, also receive information about who is at the location being querried.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class VenueDetail(Choreography):

    """
    Create a new instance of the VenueDetail Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/VenueDetail')


    def new_input_set(self):
        return VenueDetailInputSet()

    def _make_result_set(self, result, path):
        return VenueDetailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueDetailChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the VenueDetail
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class VenueDetailInputSet(InputSet):
        """
        Set the value of the ClientID input for this choreography. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the ClientSecret input for this choreography. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        def set_ClientSecret(self, value):
            InputSet._set_input(self, 'ClientSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The ID associated with the venue you want to retrieve details for.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the VenueDetail choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class VenueDetailResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class VenueDetailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VenueDetailResultSet(response, path)
