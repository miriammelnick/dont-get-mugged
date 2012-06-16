
###############################################################################
#
# AddTips
# Allows you to add a new tip at a venue. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddTips(Choreography):

    """
    Create a new instance of the AddTips Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/AddTips')


    def new_input_set(self):
        return AddTipsInputSet()

    def _make_result_set(self, result, path):
        return AddTipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTipsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddTips
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddTipsInputSet(InputSet):
        """
        Set the value of the Broadcast input for this choreography. ((optional, string) Whether to broadcast this tip. Set to "twitter" if you want to send to twitter, "facebook" if you want to send to facebook, or "twitter,facebook" if you want to send to both.)
        """
        def set_Broadcast(self, value):
            InputSet._set_input(self, 'Broadcast', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) Your Foursquare API Oauth token string.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Text input for this choreography. ((required, string) The text of the tip, up to 200 characters.)
        """
        def set_Text(self, value):
            InputSet._set_input(self, 'Text', value)

        """
        Set the value of the URL input for this choreography. ((optional, string) A URL related to this tip.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the VenueID input for this choreography. ((required, string) The venue where you want to add this tip.)
        """
        def set_VenueID(self, value):
            InputSet._set_input(self, 'VenueID', value)


"""
A ResultSet with methods tailored to the values returned by the AddTips choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddTipsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddTipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddTipsResultSet(response, path)
