
###############################################################################
#
# RetrieveBlogInfo
# Returns general information about the blog, such as the title, number of posts, and other high-level data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RetrieveBlogInfo(Choreography):

    """
    Create a new instance of the RetrieveBlogInfo Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/RetrieveBlogInfo')


    def new_input_set(self):
        return RetrieveBlogInfoInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBlogInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBlogInfoChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RetrieveBlogInfo
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RetrieveBlogInfoInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the RetrieveBlogInfo choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RetrieveBlogInfoResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Tumblr in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RetrieveBlogInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveBlogInfoResultSet(response, path)
