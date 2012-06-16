
###############################################################################
#
# RetweetedToUser
# Retrieves the 20 most recent retweets posted by users the specified user follows.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetweetedToUser(Choreography):

    """
    Create a new instance of the RetweetedToUser Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Timelines/RetweetedToUser')


    def new_input_set(self):
        return RetweetedToUserInputSet()

    def _make_result_set(self, result, path):
        return RetweetedToUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetweetedToUserChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetweetedToUser
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetweetedToUserInputSet(InputSet):
        """
        Set the value of the ContributorDetails input for this choreography. ((optional, boolean) Set to either true, t or 1 to include the screen_name of the contributor. By default only the user_id of the contributor is included.)
        """
        def set_ContributorDetails(self, value):
            InputSet._set_input(self, 'ContributorDetails', value)

        """
        Set the value of the Count input for this choreography. ((optional, integer) Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.)
        """
        def set_Count(self, value):
            InputSet._set_input(self, 'Count', value)

        """
        Set the value of the ExcludeReplies input for this choreography. ((optional, boolean) Set to either true, t or 1 to prevent replies from appearing in the returned timeline.)
        """
        def set_ExcludeReplies(self, value):
            InputSet._set_input(self, 'ExcludeReplies', value)

        """
        Set the value of the IncludeEntities input for this choreography. ((optional, boolean) An advanced option for returning more verbose metadata. When set to either true, t or 1, each tweet will include a node called "entities".)
        """
        def set_IncludeEntities(self, value):
            InputSet._set_input(self, 'IncludeEntities', value)

        """
        Set the value of the IncludeRetweets input for this choreography. ((optional, boolean) When set to either true, t or 1,the timeline will contain native retweets (if they exist) in addition to the standard stream of tweets.)
        """
        def set_IncludeRetweets(self, value):
            InputSet._set_input(self, 'IncludeRetweets', value)

        """
        Set the value of the MaxId input for this choreography. ((optional, integer) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        def set_MaxId(self, value):
            InputSet._set_input(self, 'MaxId', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((conditional, string) The Oauth Consumer Key provided by Twitter after registering your application. Required when authenticating with Oauth.)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((required, string) The Oauth Consumer Secret provided by Twitter after registering your application. Required when authenticating with Oauth.)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((conditional, string) The Oauth Token Secret retrieved during the Oauth process or provided by Twitter when registering your application. Required when authenticating with Oauth.)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((conditional, string) The Oauth Token retrieved during the Oauth process or provided by Twitter when registering your application. Required when authenticating with Oauth.)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) Specifies the page of results to retrieve.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the ScreenName input for this choreography. ((conditional, string) The screen name of the user for whom to return results for. Required unless providing a UserId.)
        """
        def set_ScreenName(self, value):
            InputSet._set_input(self, 'ScreenName', value)

        """
        Set the value of the SinceId input for this choreography. ((optional, integer) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        def set_SinceId(self, value):
            InputSet._set_input(self, 'SinceId', value)

        """
        Set the value of the TrimUser input for this choreography. ((optional, boolean) When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false.)
        """
        def set_TrimUser(self, value):
            InputSet._set_input(self, 'TrimUser', value)

        """
        Set the value of the UserId input for this choreography. ((conditional, integer) The ID of the user for whom to return results for. Required unless providing a ScreenName.)
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the RetweetedToUser choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetweetedToUserResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Twitter in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetweetedToUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetweetedToUserResultSet(response, path)
