
###############################################################################
#
# GetPhotos
# Retrieves the list of photos in a set.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetPhotos(Choreography):

    """
    Create a new instance of the GetPhotos Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Flickr/PhotoSets/GetPhotos')


    def new_input_set(self):
        return GetPhotosInputSet()

    def _make_result_set(self, result, path):
        return GetPhotosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPhotosChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetPhotos
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetPhotosInputSet(InputSet):
        """
        Set the value of the Media input for this choreography. ((optional, string) Filter results by media type. Possible values are all (default), photos or videos)
        """
        def set_Media(self, value):
            InputSet._set_input(self, 'Media', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((required, string) The Oauth Consumer Key provided by Flickr after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Flickr after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((required, string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((required, string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of results to return. If this argument is omitted, it defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of photos to return per page. Defaults to 500. The maximum allowed value is 500.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the PhotoSetID input for this choreography. ((required, integer) The ID of the photo set.)
        """
        def set_PhotoSetID(self, value):
            InputSet._set_input(self, 'PhotoSetID', value)

        """
        Set the value of the PrivacyFilter input for this choreography. ((optional, integer) Valid values are: 1 (public photos), 2 (private photos visible to friends), 3 (private photos visible to family), 4 (private photos visible to friends and family), 5 (completely private photos).)
        """
        def set_PrivacyFilter(self, value):
            InputSet._set_input(self, 'PrivacyFilter', value)


"""
A ResultSet with methods tailored to the values returned by the GetPhotos choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetPhotosResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Flickr)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetPhotosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPhotosResultSet(response, path)
