
###############################################################################
#
# GetComments
# Retrieves comments for a given photo on Flickr.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetComments(Choreography):

    """
    Create a new instance of the GetComments Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoComments/GetComments')


    def new_input_set(self):
        return GetCommentsInputSet()

    def _make_result_set(self, result, path):
        return GetCommentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCommentsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetComments
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetCommentsInputSet(InputSet):
        """
        Set the value of the MaxCommentDate input for this choreography. ((optional, date) The maximum date that a a comment was created. Should be formatted as a unix timestamp.)
        """
        def set_MaxCommentDate(self, value):
            InputSet._set_input(self, 'MaxCommentDate', value)

        """
        Set the value of the MinCommentDate input for this choreography. ((optional, date) The minimum date that a a comment was created. Should be formatted as a unix timestamp.)
        """
        def set_MinCommentDate(self, value):
            InputSet._set_input(self, 'MinCommentDate', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Flickr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Flickr after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the PhotoId input for this choreography. ((integer) The id of the photo to retrieve comments for)
        """
        def set_PhotoId(self, value):
            InputSet._set_input(self, 'PhotoId', value)


"""
A ResultSet with methods tailored to the values returned by the GetComments choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetCommentsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Flickr)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetCommentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCommentsResultSet(response, path)
