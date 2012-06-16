
###############################################################################
#
# NameSearch
# Basic query for a search by name, which will return a list of matching features for a specified place.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class NameSearch(Choreography):

    """
    Create a new instance of the NameSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/NameSearch')


    def new_input_set(self):
        return NameSearchInputSet()

    def _make_result_set(self, result, path):
        return NameSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return NameSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the NameSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class NameSearchInputSet(InputSet):
        """
        Set the value of the Format input for this choreography. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the Gazetteer input for this choreography. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        def set_Gazetteer(self, value):
            InputSet._set_input(self, 'Gazetteer', value)

        """
        Set the value of the MaxRows input for this choreography. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        def set_MaxRows(self, value):
            InputSet._set_input(self, 'MaxRows', value)

        """
        Set the value of the Name input for this choreography. ((required, string) One or more names of places to search for (separated by commas).)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the StartRow input for this choreography. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        def set_StartRow(self, value):
            InputSet._set_input(self, 'StartRow', value)


"""
A ResultSet with methods tailored to the values returned by the NameSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class NameSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class NameSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return NameSearchResultSet(response, path)
