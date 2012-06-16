
###############################################################################
#
# MostEmailed
# Retrieves information for the blog posts and articles that are most frequently emailed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MostEmailed(Choreography):

    """
    Create a new instance of the MostEmailed Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MostPopular/MostEmailed')


    def new_input_set(self):
        return MostEmailedInputSet()

    def _make_result_set(self, result, path):
        return MostEmailedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MostEmailedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MostEmailed
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MostEmailedInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) The API Key provided by NY Times)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

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
A ResultSet with methods tailored to the values returned by the MostEmailed choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MostEmailedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from the NY Times API)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MostEmailedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MostEmailedResultSet(response, path)
