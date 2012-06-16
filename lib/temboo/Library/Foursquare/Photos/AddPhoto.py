
###############################################################################
#
# AddPhoto
# Allows a user to add a new photo to a checkin, tip, or a venue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddPhoto(Choreography):

    """
    Create a new instance of the AddPhoto Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Photos/AddPhoto')


    def new_input_set(self):
        return AddPhotoInputSet()

    def _make_result_set(self, result, path):
        return AddPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddPhotoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddPhoto
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddPhotoInputSet(InputSet):
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
        Set the value of the Broadcast input for this choreography. ((optional, string) Whether to broadcast this photo. Set to "twitter" if you want to send to twitter, "facebook "if you want to send to facebook, or "twitter,facebook" if you want to send to both.)
        """
        def set_Broadcast(self, value):
            InputSet._set_input(self, 'Broadcast', value)

        """
        Set the value of the CheckinID input for this choreography. ((conditional, any) The ID of the checkin to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        def set_CheckinID(self, value):
            InputSet._set_input(self, 'CheckinID', value)

        """
        Set the value of the ImageFile input for this choreography. ((conditional, string) The base64 encoded image contents. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_ImageFile(self, value):
            InputSet._set_input(self, 'ImageFile', value)

        """
        Set the value of the LLAccuracy input for this choreography. ((optional, integer) Accuracy of the user's latitude and longitude, in meters.)
        """
        def set_LLAccuracy(self, value):
            InputSet._set_input(self, 'LLAccuracy', value)

        """
        Set the value of the Latitude input for this choreography. ((optional, decimal) Laitude of the user's location.)
        """
        def set_Latitude(self, value):
            InputSet._set_input(self, 'Latitude', value)

        """
        Set the value of the Longitude input for this choreography. ((optional, decimal) Longitude of the user's location.)
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
        Set the value of the TipID input for this choreography. ((conditional, string) The ID of the tip to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        def set_TipID(self, value):
            InputSet._set_input(self, 'TipID', value)

        """
        Set the value of the VenueID input for this choreography. ((conditional, string) The ID of the venue to attach a photo to. One of the id fields (CheckinID, TipID, or VenueID) must be specified.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to an image in the vault. Required unless specifying the ImageFile input variable.)
        """


"""
A ResultSet with methods tailored to the values returned by the AddPhoto choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddPhotoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddPhotoResultSet(response, path)
