
###############################################################################
#
# TipsFromVenue
# This choreo returns tips for a particular venue written by other Foursquare users.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TipsFromVenue(Choreography):

    """
    Create a new instance of the TipsFromVenue Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/TipsFromVenue')


    def new_input_set(self):
        return TipsFromVenueInputSet()

    def _make_result_set(self, result, path):
        return TipsFromVenueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TipsFromVenueChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TipsFromVenue
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TipsFromVenueInputSet(InputSet):
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
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to retun, up to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the OauthToken input for this choreography. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Used to page through results.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) Enter: recent or popular.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The venue you want tips for.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the TipsFromVenue choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TipsFromVenueResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TipsFromVenueChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TipsFromVenueResultSet(response, path)
