
###############################################################################
#
# RecentlyTaggedMedia
# Retrieves a list of recently tagged media.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RecentlyTaggedMedia(Choreography):

    """
    Create a new instance of the RecentlyTaggedMedia Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Instagram/RecentlyTaggedMedia')


    def new_input_set(self):
        return RecentlyTaggedMediaInputSet()

    def _make_result_set(self, result, path):
        return RecentlyTaggedMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecentlyTaggedMediaChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RecentlyTaggedMedia
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecentlyTaggedMediaInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((conditional, string) The access token retrieved during the Oauth 2.0 process. Required unless you provide the ClientID.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the ClientID input for this choreography. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the MaxID input for this choreography. ((optional, integer) Returns media earlier than this max_id.)
        """
        def set_MaxID(self, value):
            InputSet._set_input(self, 'MaxID', value)

        """
        Set the value of the MinID input for this choreography. ((optional, integer) Returns media later than this min_id.)
        """
        def set_MinID(self, value):
            InputSet._set_input(self, 'MinID', value)

        """
        Set the value of the TagName input for this choreography. ((required, string) Enter a valid tag identifier, such as: nofliter)
        """
        def set_TagName(self, value):
            InputSet._set_input(self, 'TagName', value)


"""
A ResultSet with methods tailored to the values returned by the RecentlyTaggedMedia choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecentlyTaggedMediaResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((json) The response from Instagram.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RecentlyTaggedMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecentlyTaggedMediaResultSet(response, path)
