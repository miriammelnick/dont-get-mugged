
###############################################################################
#
# RetrievePublishedPosts
# Retrieves published posts using various search and filter parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrievePublishedPosts(Choreography):

    """
    Create a new instance of the RetrievePublishedPosts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/RetrievePublishedPosts')


    def new_input_set(self):
        return RetrievePublishedPostsInputSet()

    def _make_result_set(self, result, path):
        return RetrievePublishedPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrievePublishedPostsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrievePublishedPosts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrievePublishedPostsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The Oauth Consumer Key provided by Tumblr after registering your application)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the BaseHostname input for this choreography. ((string) The standard or custom blog hostname (i.e. temboo.tumblr.com))
        """
        def set_BaseHostname(self, value):
            InputSet._set_input(self, 'BaseHostname', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) Specifies the post format to return. Valid values are: text (Plain text, no HTML), raw (As entered by user). HTML is returned when left null.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the ID input for this choreography. ((optional, integer) The specified post ID in order to return a single post.)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the Limit input for this choreography. ((optional, integer) The number of posts to return: 1- 20. Defaults to 20.)
        """
        def set_Limit(self, value):
            InputSet._set_input(self, 'Limit', value)

        """
        Set the value of the NotesInfo input for this choreography. ((optional, boolean) Indicates whether to return notes information (specify true or false). Defaults to 0 (false).)
        """
        def set_NotesInfo(self, value):
            InputSet._set_input(self, 'NotesInfo', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The post number to start at. Defaults to 0.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ReblogInfo input for this choreography. ((optional, boolean) Indicates whether to return reblog information (specify 1 or 0). Defaults to 0 (false).)
        """
        def set_ReblogInfo(self, value):
            InputSet._set_input(self, 'ReblogInfo', value)

        """
        Set the value of the Tag input for this choreography. ((optional, string) Limits the response to posts with the specified tag)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The type of post to return. Specify one of the following:  text, quote, link, answer, video, audio, photo. When null, all types are returned.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)


"""
A ResultSet with methods tailored to the values returned by the RetrievePublishedPosts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrievePublishedPostsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Tumblr in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrievePublishedPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrievePublishedPostsResultSet(response, path)
