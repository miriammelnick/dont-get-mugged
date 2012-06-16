
###############################################################################
#
# FacesStatus
# Retrieve training status for provided user IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FacesStatus(Choreography):

    """
    Create a new instance of the FacesStatus Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/FacesStatus')


    def new_input_set(self):
        return FacesStatusInputSet()

    def _make_result_set(self, result, path):
        return FacesStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FacesStatusChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FacesStatus
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FacesStatusInputSet(InputSet):
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
        Set the value of the CallbackURL input for this choreography. ((optional, string) Invoke the method, and POST the response to the specified URL. For additional information, see the Choreo documentation.)
        """
        def set_CallbackURL(self, value):
            InputSet._set_input(self, 'CallbackURL', value)

        """
        Set the value of the Callback input for this choreography. ((optional, string) Enter a javascript method to wrap a JSON-formatted response for JSONP support.  This call is ignored if ResponseFormat=xml.)
        """
        def set_Callback(self, value):
            InputSet._set_input(self, 'Callback', value)

        """
        Set the value of the Namespace input for this choreography. ((optional, string) Enter a default user if using short-hand syntax (only the user ID, without adding the @namespace))
        """
        def set_Namespace(self, value):
            InputSet._set_input(self, 'Namespace', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml.  Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the UIDs input for this choreography. ((required, string) Enter the user IDs to search for in the photo(s) being passed in the request.)
        """
        def set_UIDs(self, value):
            InputSet._set_input(self, 'UIDs', value)

        """
        Set the value of the UserAuth input for this choreography. ((optional, string) Use to access Facebook and Twitter resources for tagging.  Enter name:value pairs, comma-separated. EXAMPLE fb_user:[facebook user_id].)
        """
        def set_UserAuth(self, value):
            InputSet._set_input(self, 'UserAuth', value)


"""
A ResultSet with methods tailored to the values returned by the FacesStatus choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FacesStatusResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FacesStatusChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FacesStatusResultSet(response, path)
