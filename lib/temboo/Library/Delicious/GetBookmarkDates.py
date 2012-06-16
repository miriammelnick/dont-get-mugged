
###############################################################################
#
# GetBookmarkDates
# Retrieve a list of dates, with the number of bookmarks posted for each date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetBookmarkDates(Choreography):

    """
    Create a new instance of the GetBookmarkDates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Delicious/GetBookmarkDates')


    def new_input_set(self):
        return GetBookmarkDatesInputSet()

    def _make_result_set(self, result, path):
        return GetBookmarkDatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBookmarkDatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetBookmarkDates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetBookmarkDatesInputSet(InputSet):
        """
        Set the value of the Password input for this choreography. ((string) The password that corresponds to the specified Delicious account username.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Tags input for this choreography. ((optional, string) Return only items tagged with the specified keyword.)
        """
        def set_Tags(self, value):
            InputSet._set_input(self, 'Tags', value)

        """
        Set the value of the Username input for this choreography. ((string) A valid Delicious account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetBookmarkDates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetBookmarkDatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response returned from Delicious.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetBookmarkDatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBookmarkDatesResultSet(response, path)
