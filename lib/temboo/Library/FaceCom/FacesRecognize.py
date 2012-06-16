
###############################################################################
#
# FacesRecognize
# Detect and recognize one or more user ID's faces in specified photos submitted via a URL(s).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class FacesRecognize(Choreography):

    """
    Create a new instance of the FacesRecognize Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/FacesRecognize')


    def new_input_set(self):
        return FacesRecognizeInputSet()

    def _make_result_set(self, result, path):
        return FacesRecognizeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FacesRecognizeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the FacesRecognize
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class FacesRecognizeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) Enter your face.com API Key.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the APISecret input for this choreography. ((required, string) Enter your Face.com API Secret.)
        """
        def set_APISecret(self, value):
            InputSet._set_input(self, 'APISecret', value)

        """
        Set the value of the Attributes input for this choreography. ((optional, string) Specify attributes returned: all, none, or a list of comma-separated attributes. Default attributes returned are: gender, glasses, smiling.)
        """
        def set_Attributes(self, value):
            InputSet._set_input(self, 'Attributes', value)

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
        Set the value of the Detector input for this choreography. ((optional, string) Specify the face detector work mode.  Enter: Normal (default), or Aggressive. Note that using Aggressive counts as two Normal detections.)
        """
        def set_Detector(self, value):
            InputSet._set_input(self, 'Detector', value)

        """
        Set the value of the Namespace input for this choreography. ((optional, string) Enter a default user if using short-hand syntax (only the user ID, without adding the @namespace).)
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
        Set the value of the URLs input for this choreography. ((required, string) A comma-separated list of JPG photos to be tagged.)
        """
        def set_URLs(self, value):
            InputSet._set_input(self, 'URLs', value)


"""
A ResultSet with methods tailored to the values returned by the FacesRecognize choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class FacesRecognizeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class FacesRecognizeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FacesRecognizeResultSet(response, path)
