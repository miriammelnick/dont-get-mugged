
###############################################################################
#
# CreateEmbedLink
# Creates a previewer embed link for a Box.net file you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEmbedLink(Choreography):

    """
    Create a new instance of the CreateEmbedLink Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/CreateEmbedLink')


    def new_input_set(self):
        return CreateEmbedLinkInputSet()

    def _make_result_set(self, result, path):
        return CreateEmbedLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEmbedLinkChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEmbedLink
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEmbedLinkInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AllowDownload input for this choreography. ((optional, boolean) Enter "1" to add a direct download button to the preview, or "0" (the default) to not add a button.)
        """
        def set_AllowDownload(self, value):
            InputSet._set_input(self, 'AllowDownload', value)

        """
        Set the value of the AllowPrint input for this choreography. ((optional, boolean) Enter "1" to add a print button to the preview, or "0" (the default) to not add a print button.)
        """
        def set_AllowPrint(self, value):
            InputSet._set_input(self, 'AllowPrint', value)

        """
        Set the value of the AllowShare input for this choreography. ((optional, boolean) Enter "1" to add a button to generate a shared link to the file in the preview, or "0" (the default) to not add a button.)
        """
        def set_AllowShare(self, value):
            InputSet._set_input(self, 'AllowShare', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Color input for this choreography. ((optional, string) The hexidecimal value of the previewer background color. The default is 9E9E9E (grey).)
        """
        def set_Color(self, value):
            InputSet._set_input(self, 'Color', value)

        """
        Set the value of the FileID input for this choreography. ((required, string) The Box.net ID of the file for which you want to create an embedded preview link.)
        """
        def set_FileID(self, value):
            InputSet._set_input(self, 'FileID', value)

        """
        Set the value of the Height input for this choreography. ((optional, integer) The height in pixels of the previewer. The default is 600.)
        """
        def set_Height(self, value):
            InputSet._set_input(self, 'Height', value)

        """
        Set the value of the Width input for this choreography. ((optional, integer) The width in pixels of the previewer. The default is 600.)
        """
        def set_Width(self, value):
            InputSet._set_input(self, 'Width', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEmbedLink choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEmbedLinkResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "EmbedLink" output from this choreography execution. ((string) The embed link returned by Box.net.)
        """
        def get_EmbedLink(self):
            return self._output.get('EmbedLink', None)

class CreateEmbedLinkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEmbedLinkResultSet(response, path)
