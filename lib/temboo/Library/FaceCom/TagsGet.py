
###############################################################################
#
# TagsGet
# Display saved tags in photos that have been uploaded via a URL, or for a specified User ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class TagsGet(Choreography):

    """
    Create a new instance of the TagsGet Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FaceCom/TagsGet')


    def new_input_set(self):
        return TagsGetInputSet()

    def _make_result_set(self, result, path):
        return TagsGetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TagsGetChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the TagsGet
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class TagsGetInputSet(InputSet):
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
        Set the value of the Filter input for this choreography. ((optional, string) Filter results using the following format and options: gender:male/female. For additional options see Choreo documentation.)
        """
        def set_Filter(self, value):
            InputSet._set_input(self, 'Filter', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) Enter the maximum number of tags to be returned. Default: 5.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the Namespace input for this choreography. ((optional, string) Enter a default user namespace to be used for all users specified in teh short-hand syntax (user ID, without '@namespace').)
        """
        def set_Namespace(self, value):
            InputSet._set_input(self, 'Namespace', value)

        """
        Set the value of the Order input for this choreography. ((optional, string) Enter: recent, or random.)
        """
        def set_Order(self, value):
            InputSet._set_input(self, 'Order', value)

        """
        Set the value of the PIDs input for this choreography. ((optional, string) Enter photo IDs to retrieve tags from.)
        """
        def set_PIDs(self, value):
            InputSet._set_input(self, 'PIDs', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) You have the option of selecting json or xml.  Defaults to xml.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Together input for this choreography. ((optional, string) If specifying multiple UIDs, return only those photos where ALL UIDs appear together in the photo. Default: false.)
        """
        def set_Together(self, value):
            InputSet._set_input(self, 'Together', value)

        """
        Set the value of the UIDs input for this choreography. ((optional, string) Enter a comma-separated list of user IDs to retrieve.)
        """
        def set_UIDs(self, value):
            InputSet._set_input(self, 'UIDs', value)

        """
        Set the value of the URLs input for this choreography. ((optional, string) A comma-separated list of JPG photos to be tagged.)
        """
        def set_URLs(self, value):
            InputSet._set_input(self, 'URLs', value)

        """
        Set the value of the UserAuth input for this choreography. ((optional, string) Use to access Facebook and Twitter resources for tagging.  Enter name:value pairs, comma-separated. EXAMPLE fb_user:[facebook user_id].)
        """
        def set_UserAuth(self, value):
            InputSet._set_input(self, 'UserAuth', value)


"""
A ResultSet with methods tailored to the values returned by the TagsGet choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class TagsGetResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Face.com. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class TagsGetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TagsGetResultSet(response, path)
