
###############################################################################
#
# TagsAdd
# Manually add a face tag to a photo.  Manually-added tags are not used to train the Face.com detection system.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TagsAdd(Choreography):

    """
    Create a new instance of the TagsAdd Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/TagsAdd')


    def new_input_set(self):
        return TagsAddInputSet()

    def _make_result_set(self, result, path):
        return TagsAddResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagsAddChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TagsAdd
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TagsAddInputSet(InputSet):
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
        Set the value of the Callback input for this choreography. ((optional, string) Enter a javascript method to wrap a JSON-formatted response for JSONP support.  This call is ignored if ResponseFormat=xml)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the Height input for this choreography. ((required, integer) Enter the height of the tag, as a percentage from 0 to 100.)
        """
        def set_Height(self, value):
            InputSet._set_input(self, 'Height', value)

        """
        Set the value of the Label input for this choreography. ((optional, string) The name of the user being displayed.  Usually, this in the format: First and Last name).)
        """
        def set_Label(self, value):
            InputSet._set_input(self, 'Label', value)

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
        Set the value of the TaggerID input for this choreography. ((required, string) Enter the ID of the user who is adding the tag.)
        """
        def set_TaggerID(self, value):
            InputSet._set_input(self, 'TaggerID', value)

        """
        Set the value of the UID input for this choreography. ((required, string) Enter the ID of the user being tagged in the format: userID@namespace)
        """
        def set_UID(self, value):
            InputSet._set_input(self, 'UID', value)

        """
        Set the value of the URL input for this choreography. ((required, string) Enter the URL of the photo to be tagged.)
        """
        def set_URL(self, value):
            InputSet._set_input(self, 'URL', value)

        """
        Set the value of the UserAuth input for this choreography. ((optional, string) Use to access Facebook and Twitter resources for tagging.  Enter name:value pairs, comma-separated. EXAMPLE fb_user:[facebook user_id].)
        """
        def set_UserAuth(self, value):
            InputSet._set_input(self, 'UserAuth', value)

        """
        Set the value of the Width input for this choreography. ((required, integer) Enter the width of the tag, as a percentage from 0 to 100.)
        """
        def set_Width(self, value):
            InputSet._set_input(self, 'Width', value)

        """
        Set the value of the X input for this choreography. ((required, integer) Enter the horizontal position of the tag, as a percentage from 0 to 100, measured from the left of the photo.)
        """
        def set_X(self, value):
            InputSet._set_input(self, 'X', value)

        """
        Set the value of the Y input for this choreography. ((required, integer) Enter the veritcal position of the tag, as a percentage from 0 to 100, measured from the top of the photo.)
        """
        def set_Y(self, value):
            InputSet._set_input(self, 'Y', value)


"""
A ResultSet with methods tailored to the values returned by the TagsAdd choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TagsAddResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TagsAddChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TagsAddResultSet(response, path)
