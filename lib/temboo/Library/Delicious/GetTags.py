
###############################################################################
#
# GetTags
# Retrieves a list of all tags and the number of bookmarks that use them.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetTags(Choreography):

    """
    Create a new instance of the GetTags Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetTags')


    def new_input_set(self):
        return GetTagsInputSet()

    def _make_result_set(self, result, path):
        return GetTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTagsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetTags
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetTagsInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetTags choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetTagsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTagsResultSet(response, path)
