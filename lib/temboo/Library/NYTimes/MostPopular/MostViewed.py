
###############################################################################
#
# MostViewed
# Retrieves information for the blog posts and articles that are most frequently viewed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MostViewed(Choreography):

    """
    Create a new instance of the MostViewed Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MostPopular/MostViewed')


    def new_input_set(self):
        return MostViewedInputSet()

    def _make_result_set(self, result, path):
        return MostViewedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MostViewedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MostViewed
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MostViewedInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The API Key provided by NY Times)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The starting point of the result set. Must be a multiple of 20.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the Section input for this choreography. ((string) Limits the results by one or more sections (i.e. arts).  To get all sections, specify all-sections.)
        """
        def set_Section(self, value):
            InputSet._set_input(self, 'Section', value)

        """
        Set the value of the TimePeriod input for this choreography. ((integer) Corresponds to a day, a week, or a month of content (i.e. 1, 7, 30))
        """
        def set_TimePeriod(self, value):
            InputSet._set_input(self, 'TimePeriod', value)


"""
A ResultSet with methods tailored to the values returned by the MostViewed choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MostViewedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MostViewedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MostViewedResultSet(response, path)
