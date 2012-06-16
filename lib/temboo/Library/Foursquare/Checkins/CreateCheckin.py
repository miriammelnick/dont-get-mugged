
###############################################################################
#
# CreateCheckin
# Allows you to create a checkin with Foursquare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateCheckin(Choreography):

    """
    Create a new instance of the CreateCheckin Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/CreateCheckin')


    def new_input_set(self):
        return CreateCheckinInputSet()

    def _make_result_set(self, result, path):
        return CreateCheckinResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCheckinChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateCheckin
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateCheckinInputSet(InputSet):
        """
        Set the value of the AccuracyOfCoordinates input for this choreography. ((optional, integer) Accuracy of the user's latitude and longitude, in meters.)
        """
        def set_AccuracyOfCoordinates(self, value):
            InputSet._set_input(self, 'AccuracyOfCoordinates', value)

        """
        Set the value of the AltitudeAccuracy input for this choreography. ((optional, integer) Vertical accuracy of the user's location, in meters.)
        """
        def set_AltitudeAccuracy(self, value):
            InputSet._set_input(self, 'AltitudeAccuracy', value)

        """
        Set the value of the Altitude input for this choreography. ((optional, integer) Altitude of the user's location, in meters.)
        """
        def set_Altitude(self, value):
            InputSet._set_input(self, 'Altitude', value)

        """
        Set the value of the Broadcast input for this choreography. ((optional, string) Who to broadcast this check-in to. Can be a comma-delimited list: private, public, facebook, twitter, or followers. Defaults to 'public'.)
        """
        def set_Broadcast(self, value):
            InputSet._set_input(self, 'Broadcast', value)

        """
        Set the value of the EventID input for this choreography. ((optional, string) The event the user is checking in to. A venueId for a venue with this eventId must also be specified in the request.)
        """
        def set_EventID(self, value):
            InputSet._set_input(self, 'EventID', value)

        """
        Set the value of the Latitude input for this choreography. ((optional, decimal) The latitude point of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((optional, decimal) The longitude point of the user's location.)
        """
        def set_Longitude(self, value):
            InputSet._set_input(self, 'Longitude', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The FourSquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Shout input for this choreography. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        def set_Shout(self, value):
            InputSet._set_input(self, 'Shout', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The venue where the user is checking in. No venueid is needed if shouting or just providing a venue name.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)

        """
        Set the value of the Venue input for this choreography. ((optional, string) If you are not shouting, but you don't have a venue ID or prefer a 'venueless' checkin, pass the venue name as a string using this parameter.)
        """
        def set_Venue(self, value):
            InputSet._set_input(self, 'Venue', value)


"""
A ResultSet with methods tailored to the values returned by the CreateCheckin choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateCheckinResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateCheckinChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCheckinResultSet(response, path)
