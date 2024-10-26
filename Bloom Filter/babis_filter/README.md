# Αλλαγές που έκανα:
<ul>
  
  <li>static methods instead of class methods:</li>
        <ul><li>Τα _calculate_bit_array_size και _calculate_num_hash έγιναν @staticmethods επειδή δεν χρειάζονται class ή instance attributes.</li></ul><br>
  
  <li>adding an extra method:</li>
        <ul><li>Η μέθοδος add_elements είναι μια βοηθητική μέθοδος που προσθέτει πολλαπλά στοιχεία στο Bloom Filter ταυτόχρονα, βελτιώνοντας την αναγνωσιμότητα(readability) του test file.</li></li></ul><br>
  
  <li>improved naming:</li>
        <ul><li>Μετονόμασα την filter_element σε add και την check_element σε contains.</li></ul><br>

</ul>
