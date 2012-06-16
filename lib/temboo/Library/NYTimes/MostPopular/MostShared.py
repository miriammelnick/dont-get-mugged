
###############################################################################
#
# MostShared
# Retrieves information for the blog posts and articles that are most frequently shared.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MostShared(Choreography):

    """
    Create a new instance of the MostShared Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MostPopular/MostShared')


    def new_input_set(self):
        return MostSharedInputSet()

    def _make_result_set(self, result, path):
        return MostSharedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MostSharedChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MostShared
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MostSharedInputSet(InputSet):
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
        Set the value of the ShareTypes input for this choreography. ((string) Limits the results by the method used to share the items.  Separate multiple share types by semicolons (i.e. facebook; twitter).)
        """
        def set_ShareTypes(self, value):
            InputSet._set_input(self, 'ShareTypes', value)

        """
        Set the value of the TimePeriod input for this choreography. ((integer) Corresponds to a day, a week, or a month of content (i.e. 1, 7, 30))
        """
        def set_TimePeriod(self, value):
            InputSet._set_input(self, 'TimePeriod', value)


"""
A ResultSet with methods tailored to the values returned by the MostShared choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MostSharedResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from the NY Times API)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MostSharedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MostSharedResultSet(response, path)
