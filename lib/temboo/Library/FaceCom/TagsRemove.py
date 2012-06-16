
###############################################################################
#
# TagsRemove
# Remove a previously saved face tag from a photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TagsRemove(Choreography):

    """
    Create a new instance of the TagsRemove Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/TagsRemove')


    def new_input_set(self):
        return TagsRemoveInputSet()

    def _make_result_set(self, result, path):
        return TagsRemoveResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagsRemoveChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TagsRemove
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TagsRemoveInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your Face.com API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Enter your Face.com API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) Enter a javascript method to wrap a JSON-formatted response for JSONP support.  This call is ignored if ResponseFormat=xml.)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the Password input for this choreography. ((optional, string) must be enabled in application settings] Use when saving tags is specified to be a priviledged action in your application.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml.  Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the TIDs input for this choreography. ((required, string) Enter at least one tag ID, obtained from FacesDetect or FacesRecognized choreos. The tag ID will be associated with the user ID (UID).)
        """
        def set_TIDs(self, value):
            InputSet._set_input(self, 'TIDs', value)

        """
        Set the value of the TaggerID input for this choreography. ((required, string) Enter the user ID of the tagger.)
        """
        def set_TaggerID(self, value):
            InputSet._set_input(self, 'TaggerID', value)

        """
        Set the value of the UserAuth input for this choreography. ((optional, string) Use to access Facebook and Twitter resources for tagging.  Enter name:value pairs, comma-separated. EXAMPLE fb_user:[facebook user_id].)
        """
        def set_UserAuth(self, value):
            InputSet._set_input(self, 'UserAuth', value)


"""
A ResultSet with methods tailored to the values returned by the TagsRemove choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TagsRemoveResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TagsRemoveChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TagsRemoveResultSet(response, path)
