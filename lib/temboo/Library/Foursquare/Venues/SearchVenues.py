
###############################################################################
#
# SearchVenues
# Obtain a list of venues near the current location. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchVenues(Choreography):

    """
    Create a new instance of the SearchVenues Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/SearchVenues')


    def new_input_set(self):
        return SearchVenuesInputSet()

    def _make_result_set(self, result, path):
        return SearchVenuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchVenuesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchVenues
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchVenuesInputSet(InputSet):
        """
        Set the value of the AccuracyOfCoordinates input for this choreography. ((optional, integer) Accuracy of latitude and longitude, in meters. Currently, this parameter   does not affect search results.)
        """
        def set_AccuracyOfCoordinates(self, value):
            InputSet._set_input(self, 'AccuracyOfCoordinates', value)

        """
        Set the value of the AltitudeAccuracy input for this choreography. ((optional, integer) Accuracy of the user's altitude, in meters. Currently, this parameter does not affect search results.)
        """
        def set_AltitudeAccuracy(self, value):
            InputSet._set_input(self, 'AltitudeAccuracy', value)

        """
        Set the value of the Altitude input for this choreography. ((optional, integer) Altitude of the user's location, in meters. Currently, this parameter does not affect search results.)
        """
        def set_Altitude(self, value):
            InputSet._set_input(self, 'Altitude', value)

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
        Set the value of the Intent input for this choreography. ((optional, string) Indicates your intent when performing the search.  Enter: checkin (default), match (requires Query and Latitude/Longitude to be provided).)
        """
        def set_Intent(self, value):
            InputSet._set_input(self, 'Intent', value)

        """
        Set the value of the Latitude input for this choreography. ((required, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Number of results to retun, up to 50.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Longitude input for this choreography. ((required, decimal) The longitude point of the user's location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthToken input for this choreography. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) Your search string.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the SearchVenues choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchVenuesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchVenuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchVenuesResultSet(response, path)
